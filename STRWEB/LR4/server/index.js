require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const passport = require('passport');
const path = require('path');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(passport.initialize());

// Static files
app.use('/uploads', express.static('uploads'));

// Маршруты API
app.use('/api/upload', require('./routes/upload'));  // Добавьте эту строку
app.use('/api/auth', require('./routes/auth'));
app.use('/api/parts', require('./routes/parts'));

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/autoshop', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Routes (будут добавлены позже)
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to AutoShop 