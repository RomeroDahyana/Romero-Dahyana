// src/Login.js
import React , {useState} from 'react';
import "./Login.css";
import { Link, useNavigate} from 'react-router-dom';
import Cabecera from '../Cabecera/Cabecera';
import { useAuth } from './Componentes/Login/UserAuth';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const { login } = useAuth(); 
  
  const [errorMessage, setErrorMessage] = useState('');

// ...

try {
  // ... (código existente)
} catch (error) {
  setErrorMessage(error.message);
}

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Aquí puedes manejar el inicio de sesión como desees, por ejemplo, llamar a una API.
    // Redirige a Home después de iniciar sesión, o maneja errores de autenticación aquí.
    navigate('/Home');
    
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        throw new Error('Credenciales incorrectas');
      }

      const data = await response.json();
      localStorage.setItem('token', data.token);
      login(); // Establece que el usuario ha iniciado sesión
      navigate('/Home');
    } catch (error) {
      setErrorMessage(error.message) ;
    }
  };
  

  return (
    <div className='login-container'> 
      <div><Cabecera/></div>
      <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
              <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0m4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4m-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10s-3.516.68-4.168 1.332c-.678.678-.83 1.418-.832 1.664z"/>
      </svg>
      <h1>INICIAR SESIÓN</h1>

      <form onSubmit={handleSubmit}>
        <div className='input-group'>
            <div >
              <label htmlFor="username">Usuario:</label>
              <input type="text" id="username" value={username}  onChange={(e) => setUsername(e.target.value)}
              required />
            </div>
            <div >
              <label htmlFor="password">Contraseña:</label>
              <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)}
              required />
            </div>
        </div>
        <button type="submit">Ingresar</button>
      </form>
      <p className='register-prompt'> ¿No tienes una cuenta? <Link to="/registro">¡Regístrate ahora!</Link></p>
      
    </div>
  );
};

export default Login;