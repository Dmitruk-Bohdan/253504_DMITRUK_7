import express from 'express';
import jwt from 'jsonwebtoken';
import mongoose from 'mongoose';

const dbConnectUri = "mongodb+srv://user:1111@cluster0.ctei9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

mongoose
    .connect(dbConnectUri)
    .then(() => console.log('DB OK'))
    .catch((err) => console.log('DB error: ', err));

const app = express();

app.use(express.json());

app.get('/', (req, res) =>{
    res.send('Amerika nya! Haro!')
});

app.post('/auth/login', (req, res) =>
{
    const token = jwt.sign({
        email: req.body.email,
        name: 'ваяс пупкин',
    },
    'somesecret1525');
    res.json({
        success : true,
        token,
    });
});

app.listen(4444, (err) =>{
    if(err)
    {
        return console.log(err)
    }
    console.log('Server OK');
});