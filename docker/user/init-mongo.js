print("Started Adding the Users.");
db = db.getSiblingDB("admin");
db.createUser({
  user: "marc",
  pwd: "test",
  roles: [{ role: "readWrite", db: "admin"}],
});
print("End Adding the User Roles.");