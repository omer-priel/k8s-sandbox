# Description: Update the /etc/hosts file with the local domains (*.test).
# Python Version: 3.10

import argparse


CONFIG_FILE_LOCATION = '/etc/hosts'
FIRST_LINE = '# k8s-sandbox: Local Domains\n'
LAST_LINE = '# k8s-sandbox: End of Local Domains\n'

DOMAINS = [
    'mongo-express.test',

    'nginx-example.test',
    'express-example.test',
    'fastapi-example.test',
    'flask-example.test',
    'fastify-example.test',
    'gohttp-example.test',
    'gin-example.test',
    'django-example.test',
]

parser = argparse.ArgumentParser(
    description='Update the /etc/hosts file with the local domains (*.test).'
)

actions_subparsers = parser.add_subparsers(
    title='actions',
    dest='action',
)

show_parser = actions_subparsers.add_parser(
    'show',
    help='Show the current section in the /etc/hosts file and the local domains.'
)

update_parser = actions_subparsers.add_parser(
    'update',
    help='Update the /etc/hosts file with the local domains.'
)

update_parser.add_argument(
    'minikube_ip',
    type=str,
    help='Minikube IP address to use for the local domains.'
)


def get_current_project_section() -> tuple[list[str], str | None]:
    with open(CONFIG_FILE_LOCATION, 'r') as file:
        lines = file.readlines()

    lines = list(lines)

    found_section = False
    project_section = False

    section_lines = []

    for line in lines:
        if line == FIRST_LINE:
            if not project_section:
                project_section = True
                if found_section:
                    return [], 'Found multiple sections of the project in the /etc/hosts file.'
                found_section = True
            else:
                return [], 'Found multiple sections of the project in the /etc/hosts file.'
        elif line == LAST_LINE:
            if project_section:
                project_section = False
            else:
                return [], 'Found end of project section without the start of the section.'
        elif project_section:
            line = line.strip()
            if line:
                section_lines.append(line)

    if project_section:
        return [], 'Found start of project section without the end of the section.'

    return section_lines, None


def show_command() -> None:
    section_lines, error = get_current_project_section()

    if error is not None:
        print(f'Error: {error}\n')
        return

    print('Current Section in /etc/hosts:')
    if not section_lines:
        print('No lines found.')
    for line in section_lines:
        print(line)
    print('')

    print('Project Local Domains:')
    if not DOMAINS:
        print('No domains found.')
    for domain in DOMAINS:
        print(domain)
    print('')


def update_command(minikube_ip: str) -> None:
    # validate
    ip_parts = minikube_ip.split('.')
    if len(ip_parts) != 4:
        print('Error: Invalid IP address format.\n')
        return

    if not all(part.isdigit() for part in ip_parts):
        print('Error: Invalid IP address format.\n')
        return

    _, error = get_current_project_section()

    if error is not None:
        print(f'Error: {error}\n')
        return

    # update the file

    with open(CONFIG_FILE_LOCATION, 'r') as file:
        file_lines = file.readlines()

    with open(CONFIG_FILE_LOCATION, 'w') as file:
        project_section = False
        for i, line in enumerate(file_lines):
            if line == FIRST_LINE:
                project_section = True
            elif project_section:
                if line == LAST_LINE:
                    project_section = False
            else:
                if i < len(file_lines) - 1:
                    file.write(line)

        file.write(FIRST_LINE)
        file.write('\n')
        for domain in DOMAINS:
            file.write(f'{minikube_ip} {domain}\n')
        file.write('\n')
        file.write(LAST_LINE)


def main() -> None:
    args = parser.parse_args()

    if args.action == 'show':
        show_command()
    elif args.action == 'update':
        update_command(args.minikube_ip)


if __name__ == '__main__':
    main()
