// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import { AuthProvider } from './Componentes/Admin/AuthContext.js'; // Asegúrate de que la ruta es correcta
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);
