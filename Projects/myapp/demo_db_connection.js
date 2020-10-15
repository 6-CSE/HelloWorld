var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "mysql",
  password: "Gw@lior2001"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});