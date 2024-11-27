const mongoose = require('mongoose');

const partSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        maxLength: 100
    },
    articleNumber: {
        type: String,
        required: true,
        maxLength: 20,
        unique: true
    },
    description: {
        type: String,
        required: true,
        maxLength: 1000
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    images: [{
        type: String,
        required: true
    }],
    category: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Category',
        required: true
    },
    stock: {
        type: Number,
        default: 5,
        min: 0
    }
}, { timestamps: true });

module.exports = mongoose.model('Part', partSchema);
