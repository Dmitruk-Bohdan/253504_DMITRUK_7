const mongoose = require('mongoose');

const promoCodeSchema = new mongoose.Schema({
    code: {
        type: String,
        required: true,
        unique: true,
        maxLength: 20
    },
    discount: {
        type: Number,
        required: true,
        min: 0,
        max: 100
    },
    expirationDate: {
        type: Date,
        required: true,
        default: () => new Date(+new Date() + 30*24*60*60*1000) // +30 days
    },
    isActive: {
        type: Boolean,
        default: true
    }
}, { timestamps: true });

module.exports = mongoose.model('PromoCode', promoCodeSchema);
