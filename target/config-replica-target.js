rsconf = {
    _id: "rs1",
    members: [{ _id: 0, host: "mongo-target:27017", priority: 1.0 }],
  };
  rs.initiate(rsconf);
  rs.status();
