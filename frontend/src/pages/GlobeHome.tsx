import React from 'react';
import CesiumGlobe from '../components/CesiumGlobe';
import { useTranslation } from 'react-i18next';

const GlobeHome = () => {
  const { t } = useTranslation();

  return (
    <div>
      <h1>{t('app.title')}</h1>
      <p>{t('globe.home')}</p>
      <CesiumGlobe />
    </div>
  );
};

export default GlobeHome;