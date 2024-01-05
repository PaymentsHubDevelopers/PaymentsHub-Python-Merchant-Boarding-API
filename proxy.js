const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const port = 3001;

app.use(express.json());
app.use(cors());

let token = '';
const authUrl = 'https://enrollment-api-auth.paymentshub.com/oauth/token';
const payloadUrl = 'https://enrollment-api-sandbox.paymentshub.com/enroll/application';
const data = {
  grant_type: 'client_credentials',
  scope: 'all',
  client_id: 'your_client_id',
  client_secret: 'your_client_secret'
};
const config = {
headers: {
  'Content-Type': 'application/x-www-form-urlencoded'
}
};

const params = new URLSearchParams(data);


app.get('/oauth/token', async (req,res) => {
  try {
    axios.post(authUrl, params, config)
    .then(response => {
    console.log('Response:', response.data);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.send(response.data);
    token = response.data.access_token;
    })
    .catch(error => {
    console.error('Error:', error);
    });

  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.post('/create_application', async (req, res)=>{

    axios.post(payloadUrl, req.body, 
      {headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }})
    .then(response => {
    console.log('Response:', response.data);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.send(response.data);
    })
    .catch(error => {
      console.error('Error:', error);
      res.send(error);
    });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
