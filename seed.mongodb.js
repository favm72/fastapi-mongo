use("fastapi")
const crypto = require("crypto")

db.getCollection("account").insertMany([
  {
    id: crypto.randomUUID(),
    name: "John Doe",
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
  {
    id: crypto.randomUUID(),
    name: "Jane Doe",
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
  {
    id: crypto.randomUUID(),
    name: "John Smith",
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  },
])

use("fastapi")
db.getCollection("account").find({})
