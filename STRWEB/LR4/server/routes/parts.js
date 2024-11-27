const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const Part = require('../models/Part');
const User = require('../models/User');

// Get all parts
router.get('/', async (req, res) => {
    try {
        const parts = await Part.find().populate('category');
        res.json(parts);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server Error');
    }
});

// Add part to user's cart
router.post('/add-to-cart/:partId', auth, async (req, res) => {
    try {
        const part = await Part.findById(req.params.partId);
        if (!part) {
            return res.status(404).json({ msg: 'Part not found' });
        }

        const user = await User.findById(req.user.id);
        if (!user) {
            return res.status(404).json({ msg: 'User not found' });
        }

        // Check if part already in cart
        const cartItemIndex = user.cart.findIndex(
            item => item.part.toString() === req.params.partId
        );

        if (cartItemIndex > -1) {
            // If part exists, increment quantity
            user.cart[cartItemIndex].quantity += 1;
        } else {
            // If part doesn't exist, add it
            user.cart.push({
                part: req.params.partId,
                quantity: 1
            });
        }

        await user.save();
        res.json(user.cart);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server Error');
    }
});

module.exports = router;
