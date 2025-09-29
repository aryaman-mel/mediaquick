<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>MediQuick</title>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
  <h1>MediQuick</h1>
  <p class="warn">Not a diagnosis. For emergencies, call local services.</p>

  <section>
    <label>Enter symptoms (comma separated):</label>
    <input id="symptoms" placeholder="fever, cough, fatigue" />
    <button onclick="predict()">Get Suggestions</button>
    <pre id="predOut"></pre>
  </section>

  <section>
    <label>Near (lat,lng):</label>
    <input id="lat" value="-37.8136"/>
    <input id="lng" value="144.9631"/>
    <button onclick="nearby()">Find Clinics</button>
    <pre id="near
