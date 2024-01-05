const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    // Read the content of index.html
    fs.readFile('index.html', (err, data) => {
        if (err) {
            res.writeHead(404);
            res.end('File not found');
            return;
        }

        // Set the content type to HTML
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
    });
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
