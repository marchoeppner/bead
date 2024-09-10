print("Started Adding the Users.");
db = db.getSiblingDB("bead_development");
db.createUser({
  user: "marc",
  pwd: "test",
  roles: [{ role: "readWrite", db: "bead_development"}],
});
print("End Adding the User Roles.");