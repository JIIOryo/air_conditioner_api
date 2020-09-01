/**
 * @fileoverview index.js
 * @author JIIOryo
 */
'use strict';

const express = require('express');

const app = express();
const port = 45021;

app.get('/ping', (req, res) => {
    res.setHeader('Content-Type', 'application/json')
    res.send({});
});

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`)
})
