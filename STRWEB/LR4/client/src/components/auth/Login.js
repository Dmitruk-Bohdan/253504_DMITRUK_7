import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { login } = useAuth();

  const { email, password } = formData;

  const onChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = async e => {
    e.preventDefault();
    try {
      const success = await login(email, password);
      if (success) {
        navigate('/');
      } else {
        setError('Неверный email или пароль');
      }
    } catch (err) {
      setError('Ошибка входа. Попробуйте позже.');
    }
  };

  return (
    <div className="auth-container">
      <h2 className="auth-title">Вход в систему</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={onSubmit} className="auth-form">
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={onChange}
            required
            className="form-control"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Пароль</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={onChange}
            required
            className="form-control"
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Войти
        </button>
      </form>
      <div className="social-auth">
        <p>Или войдите через:</p>
        <div className="social-buttons">
          <button className="btn btn-google">Google</button>
          <button className="btn btn-facebook">Facebook</button>
        </div>
      </div>
    </div>
  );
};

export default Login;
