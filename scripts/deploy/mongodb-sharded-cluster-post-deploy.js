// This script is executed using `mongosh`

// SERVICE_FULL_HOST_NAME - full hostname of the service (e.g. mongodb-service.default.svc.cluster.local)
// SERVICE_PORT - port of the service
// SERVICE_REPLICAS - number of replicas in the StatefulSet of the service
// SERVICE_USER - user for the service
// SERVICE_PASSWORD - password for the service

const serviceFullHostName = process.env.SERVICE_FULL_HOST_NAME;
const servicePort = process.env.SERVICE_PORT;
const replicas = parseInt(process.env.SERVICE_REPLICAS);
const user = process.env.SERVICE_USER;
const userPassword = process.env.SERVICE_PASSWORD;

const hostname = process.env.HOSTNAME;
const hostnamePrefix = hostname.substring(0, hostname.lastIndexOf('-') + 1);

const members = [];

for (let i = 0; i < replicas; i++) {
  members.push({ _id: i, host : `${hostnamePrefix}${i}.${serviceFullHostName}:${servicePort}` });
}

// switch to admin database (mongosh)
use admin

// Create user for auth if dosn't exist
if (db.system.users.find({user: user}).count() == 0) {
  db.createUser(
    {
      user: user,
      pwd: userPassword,
      roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
  )
}

// check if the replica set is initiated
let rsInitiated = false;
try {
  rsInitiated = rs.status();
} catch (e) { }

if (!rsInitiated) {
  rs.initiate({_id: "rs0", version: 1, members: members});
} else {
  rs.reconfig({_id: "rs0", version: 1, members: members});
}

exit();
