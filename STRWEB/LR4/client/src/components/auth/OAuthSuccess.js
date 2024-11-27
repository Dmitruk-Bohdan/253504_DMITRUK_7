import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const OAuthSuccess = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { setAuthToken } = useAuth();

    useEffect(() => {
        const params = new URLSearchParams(location.search);
        const token = params.get('token');

        if (token) {
            setAuthToken(token);
            navigate('/');
        } else {
            navigate('/login');
        }
    }, [location, navigate, setAuthToken]);

    return (
        <div className="auth-container">
            <div className="loading-spinner">
                <div className="spinner"></div>
                <p>Completing authentication...</p>
            </div>
        </div>
    );
};

export default OAuthSuccess;
