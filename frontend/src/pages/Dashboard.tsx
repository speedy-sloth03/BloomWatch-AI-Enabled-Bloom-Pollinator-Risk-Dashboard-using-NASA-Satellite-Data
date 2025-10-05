import React, { useState, useEffect } from 'react';
import Map2D from '../components/Map2D';
import { useTranslation } from 'react-i18next';
import Chart from 'chart.js/auto';

interface DashboardProps { colorblind: boolean }

const Dashboard: React.FC<DashboardProps> = ({ colorblind }) => {
  const { t, i18n } = useTranslation();
  const [region] = useState('Dhaka'); // demo: fixed region
  const [date, setDate] = useState('2025-03-08');
  const [ndviSeries, setNdviSeries] = useState<{ date: string; ndvi: number }[]>([]);
  const [forecast, setForecast] = useState<any>(null);

  // Load NDVI series
  useEffect(() => {
    fetch('/data/sample_ndvi_timeseries.json')
      .then(r => r.json())
      .then(setNdviSeries)
      .catch(() => setNdviSeries([]));
  }, [region, date]);

  // Get forecast
  useEffect(() => {
    if (ndviSeries.length > 1) {
      fetch('/api/forecast', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lat: 23.7, lon: 90.4, ndvi_series: ndviSeries })
      })
        .then(r => r.json())
        .then(setForecast)
        .catch(() => setForecast(null));
    }
  }, [ndviSeries]);

  // Chart rendering
  useEffect(() => {
    if (!document.getElementById('ndviChart')) return;
    const ctx = (document.getElementById('ndviChart') as HTMLCanvasElement).getContext('2d');
    if (!ctx) return;
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ndviSeries.map(s => s.date),
        datasets: [{
          label: t('label.ndviSeries'),
          data: ndviSeries.map(s => s.ndvi),
          borderColor: colorblind ? '#E69F00' : '#005f73',
          backgroundColor: colorblind ? '#E69F00' : '#005f73',
          fill: false
        }]
      },
      options: { responsive: true, plugins: { legend: { display: true } } }
    });
  }, [ndviSeries, colorblind, t]);

  return (
    <section>
      <header>
        <h2>{t('dashboard.title')}</h2>
        <div>
          <span>{region}</span>
          <input
            type="date"
            value={date}
            onChange={e => setDate(e.target.value)}
            aria-label="Select date"
          />
          <button>{t('button.startTour')}</button>
        </div>
      </header>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        <aside style={{ flex: 1 }}>
          <Map2D region={region} colorblind={colorblind} />
          <button>{t('button.downloadCSV')}</button>
        </aside>
        <main style={{ flex: 2 }}>
          <canvas id="ndviChart" aria-label={t('label.ndviSeries')} />
          <div aria-live="polite">
            {ndviSeries.length > 0 &&
              <p>
                Peak NDVI: {Math.max(...ndviSeries.map(n => n.ndvi))} on {ndviSeries[0].date};
                predicted bloom onset {forecast?.predicted_onset} ± {forecast?.rmse} days.
              </p>
            }
          </div>
        </main>
        <aside style={{ flex: 1 }}>
          <div>
            <h4>{t('label.prediction')}</h4>
            <p>{forecast ? `${forecast.predicted_onset} (CI: ${forecast.ci_lower}–${forecast.ci_upper})` : '...'}</p>
          </div>
        </aside>
      </div>
    </section>
  );
};

export default Dashboard;