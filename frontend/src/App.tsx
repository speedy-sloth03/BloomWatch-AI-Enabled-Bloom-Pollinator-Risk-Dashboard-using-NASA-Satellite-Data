import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import GlobeHome from './pages/GlobeHome';
import Dashboard from './pages/Dashboard';
import { useTranslation } from 'react-i18next';
import './styles/variables.css';

function App() {
  const { i18n } = useTranslation();
  const [colorblind, setColorblind] = useState(false);

  const toggleLang = () => {
    i18n.changeLanguage(i18n.language === 'en' ? 'bn' : 'en');
  };

  const toggleColorblind = () => {
    setColorblind((v) => !v);
    document.body.classList.toggle('colorblind', !colorblind);
  };

  return (
    <BrowserRouter>
      <header>
        <button aria-label="Switch Language" onClick={toggleLang}>
          {i18n.language === 'en' ? 'বাংলা' : 'EN'}
        </button>
        <button aria-label="Toggle colorblind mode" onClick={toggleColorblind}>
          {colorblind ? 'Normal Mode' : 'Colorblind Mode'}
        </button>
        <a href="#main" className="skip-link">Skip to content</a>
      </header>
      <main id="main">
        <Routes>
          <Route path="/" element={<GlobeHome />} />
          <Route path="/dashboard" element={<Dashboard colorblind={colorblind} />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;