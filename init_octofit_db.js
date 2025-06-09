db.users.createIndex({ "email": 1 }, { unique: true })
// This file is for MongoDB shell, not JavaScript/TypeScript runtime
// To use: mongo < init_octofit_db.js
db = db.getSiblingDB('octofit_db');
db.createCollection("users");
db.createCollection("teams");
db.createCollection("activity");
db.createCollection("leaderboard");
db.createCollection("workouts");
db.users.createIndex({ "email": 1 }, { unique: true });
