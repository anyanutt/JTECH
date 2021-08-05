function writeToDatabase(fName, lName, batID, dayDate) {
  const { Client } = require("pg");
  const { resourceLimits } = require("worker_threads");
  const client = new Client({
    user: "postgres",
    password: "Q1nsh1hu@ng",
    hostname: "localhost",
    port: 5432,
    database: "jtech",
  });

  client
    .connect()
    .then(() => console.log("Connected successfuly"))
    .then(() =>
      client.query("INSERT INTO jtech_customerdata values ($1, $2, $3, $4)", [
        fName,
        lName,
        batID,
        dayDate,
      ])
    )
    .then(() => client.query("SELECT *  FROM jtech_customerdata;"))
    .then((results) => console.table(results.rows))
    .catch((e) => console.log(e))
    .finally(() => client.end());
}

function userInfo() {
  var firstName = document.getElementById("firstName").value;
  var lastName = document.getElementById("lastName").value;
  var battery_IDnum = document.getElementById("battery_IDnum").value;
  var todayDate = document.getElementById("todayDate").value;
  document.getElementById("fullName").onclick = console.log(
    "First name: " + firstName + " last name " + lastName
  );
  writeToDatabase(firstName, lastName, battery_IDnum, todayDate);
  alert(
    "Name of customer: " +
      firstName +
      " " +
      lastName +
      "\n" +
      "Battery ID: " +
      battery_IDnum +
      "\n" +
      "Date of switch: " +
      todayDate
  );
}
