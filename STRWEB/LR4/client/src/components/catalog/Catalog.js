import React, { useState, useEffect } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import axios from 'axios';
import './../../styles/Catalog.css';

const Catalog = () => {
    const [parts, setParts] = useState([]);
    const [snackbar, setSnackbar] = useState({
        show: false,
        message: '',
        type: 'success'
    });
    const { isAuthenticated } = useAuth();

    useEffect(() => {
        const fetchParts = async () => {
            try {
                const response = await axios.get('/api/parts');
                setParts(response.data);
            } catch (error) {
                console.error('Error fetching parts:', error);
                showSnackbar('Error loading parts', 'error');
            }
        };

        fetchParts();
    }, []);

    const handleAddToCart = async (partId) => {
        if (!isAuthenticated) {
            showSnackbar('Please log in to add items to cart', 'warning');
            return;
        }

        try {
            await axios.post(`/api/parts/add-to-cart/${partId}`);
            showSnackbar('Added to cart successfully', 'success');
        } catch (error) {
            console.error('Error adding to cart:', error);
            showSnackbar('Error adding to cart', 'error');
        }
    };

    const showSnackbar = (message, type) => {
        setSnackbar({ show: true, message, type });
        setTimeout(() => {
            setSnackbar(prev => ({ ...prev, show: false }));
        }, 3000);
    };

    return (
        <div className="catalog-container">
            <h1 className="catalog-title">Parts Catalog</h1>
            <div className="catalog-grid">
                {parts.map((part) => (
                    <div key={part._id} className="part-card">
                        <img
                            className="part-image"
                            src={part.images[0] || '/placeholder.png'}
                            alt={part.name}
                        />
                        <div className="part-content">
                            <h2 className="part-name">{part.name}</h2>
                            <p className="part-info">Article: {part.articleNumber}</p>
                            <p className="part-info">Category: {part.category?.name}</p>
                            <p className="part-price">${part.price}</p>
                            <button
                                className="add-to-cart-btn"
                                onClick={() => handleAddToCart(part._id)}
                            >
                                <svg
                                    className="cart-icon"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    strokeWidth="2"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                >
                                    <circle cx="9" cy="21" r="1" />
                                    <circle cx="20" cy="21" r="1" />
                                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
                                </svg>
                                Add to Cart
                            </button>
                        </div>
                    </div>
                ))}
            </div>
            {snackbar.show && (
                <div className={`snackbar ${snackbar.type}`}>
                    {snackbar.message}
                </div>
            )}
        </div>
    );
};

export default Catalog;
