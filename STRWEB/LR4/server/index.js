// Load environment variables first
require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const passport = require('passport');
const path = require('path');

// Get environment variables
const PORT = process.env.PORT;
const NODE_ENV = process.env.NODE_ENV;
const MONGODB_URI = process.env.MONGODB_URI;

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Initialize Passport
require('./config/passport');
app.use(passport.initialize());

// Static files
app.use('/uploads', express.static('uploads'));

// Маршруты API
app.use('/api/upload', require('./routes/upload'));  
app.use('/api/auth', require('./routes/auth'));
app.use('/api/parts', require('./routes/parts'));

// Database connection
console.log('Attempting to connect to MongoDB...');
console.log('MongoDB URI:', MONGODB_URI);

mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    retryWrites: true,
    w: 'majority'
})
.then(() => {
    console.log('Successfully connected to MongoDB!');
    console.log('Database connection state:', mongoose.connection.readyState);
    // 0 = disconnected, 1 = connected, 2 = connecting, 3 = disconnecting
})
.catch(err => {
    console.error('MongoDB connection error:');
    console.error('Error name:', err.name);
    console.error('Error message:', err.message);
    if (err.reason) console.error('Error reason:', err.reason);
    process.exit(1); // Завершаем процесс при ошибке подключения
});

// Routes (будут добавлены позже)
app.get('/', (req, res) => {
    res.json({ message: 'Welcome to AutoShop API' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start server with environment variables
if (!PORT) {
    console.error('PORT is not defined in .env file');
    process.exit(1);
}

app.listen(PORT, () => {
    console.log(`Server is running in ${NODE_ENV} mode on port ${PORT}`);
});
