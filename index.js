/**
 * @fileoverview index.js
 * @author JIIOryo
 */
'use strict';

const express = require('express');

const app = express();
const port = 45021;

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`)
})
