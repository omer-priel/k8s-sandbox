import fastify from 'fastify'

const server = fastify()

server.get('/', async (request, reply) => {
  reply.status(200).send({
    service: 'fastify-example',
    version: '0.1.0',
  });
})

server.listen({ port: 8000, host: '0.0.0.0' }, (err, address) => {
  if (err) {
    console.error(err)
    process.exit(1)
  }
  console.log(`Server listening at ${address}`)
})
