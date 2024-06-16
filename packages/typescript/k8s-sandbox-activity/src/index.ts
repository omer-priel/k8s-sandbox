export type ActivityMode = {
  service: string;
  endpoint: string;
  method: string;
  created_at: Date;
}

function createActivity(mode) {
  return {
    service: mode.service,
    endpoint: mode.endpoint,
    method: mode.method,
    created_at: new Date(),
  };
}
