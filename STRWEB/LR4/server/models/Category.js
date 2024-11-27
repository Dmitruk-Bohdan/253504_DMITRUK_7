const mongoose = require('mongoose');

const categorySchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        maxLength: 100
    },
    description: {
        type: String,
        default: "category description",
        maxLength: 200
    },
    slug: {
        type: String,
        unique: true
    }
}, { timestamps: true });

module.exports = mongoose.model('Category', categorySchema);
