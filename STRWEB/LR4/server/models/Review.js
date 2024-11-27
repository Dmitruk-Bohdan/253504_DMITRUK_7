const mongoose = require('mongoose');

const reviewSchema = new mongoose.Schema({
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    part: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Part',
        required: true
    },
    rating: {
        type: Number,
        required: true,
        min: 1,
        max: 5
    },
    title: {
        type: String,
        required: true,
        trim: true,
        maxlength: 100
    },
    comment: {
        type: String,
        required: true,
        trim: true,
        maxlength: 1000
    },
    images: [{
        type: String
    }],
    verified: {
        type: Boolean,
        default: false
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    updatedAt: {
        type: Date,
        default: Date.now
    }
});

// Обновление даты изменения перед сохранением
reviewSchema.pre('save', function(next) {
    this.updatedAt = new Date();
    next();
});

// Индекс для предотвращения дублирования отзывов
reviewSchema.index({ user: 1, part: 1 }, { unique: true });

module.exports = mongoose.model('Review', reviewSchema);
