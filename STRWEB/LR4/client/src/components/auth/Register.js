import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const Register = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    password2: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { register } = useAuth();

  const { name, email, password, password2 } = formData;

  const onChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = async e => {
    e.preventDefault();
    if (password !== password2) {
      setError('Пароли не совпадают');
      return;
    }
    try {
      const success = await register(name, email, password);
      if (success) {
        navigate('/');
      } else {
        setError('Ошибка регистрации. Возможно, email уже используется.');
      }
    } catch (err) {
      setError('Ошибка регистрации. Попробуйте позже.');
    }
  };

  return (
    <div className="auth-container">
      <h2 className="auth-title">Регистрация</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={onSubmit} className="auth-form">
        <div className="form-group">
          <label htmlFor="name">Имя</label>
          <input
            type="text"
            id="name"
            name="name"
            value={name}
            onChange={onChange}
            required
            className="form-control"
          />
        </div>
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
            minLength="6"
            className="form-control"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password2">Подтвердите пароль</label>
          <input
            type="password"
            id="password2"
            name="password2"
            value={password2}
            onChange={onChange}
            required
            minLength="6"
            className="form-control"
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Зарегистрироваться
        </button>
      </form>
      <div className="social-auth">
        <p>Или зарегистрируйтесь через:</p>
        <div className="social-buttons">
          <button className="btn btn-google">Google</button>
          <button className="btn btn-facebook">Facebook</button>
        </div>
      </div>
    </div>
  );
};

export default Register;
