import React, { useEffect, useRef } from 'react';

interface Map2DProps { region: string; colorblind: boolean }

const Map2D: React.FC<Map2DProps> = ({ region, colorblind }) => {
  const mapRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!window.L || !mapRef.current) return;
    const L = window.L;
    const map = L.map(mapRef.current).setView([23.7, 90.4], 7);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
    // Add sample marker — colorblind shape
    const markerShape = colorblind ? 'triangle' : 'circle';
    L.marker([23.7, 90.4], {
      icon: L.divIcon({
        className: `bloom-marker ${markerShape}`,
        html: `<div style="background:${colorblind ? '#E69F00' : '#005f73'};width:16px;height:16px;border-radius:${markerShape === 'circle' ? '50%' : '0'};"></div>`
      })
    }).addTo(map);
    return () => { map.remove(); };
  }, [region, colorblind]);

  return (
    <div ref={mapRef} id="map2d" style={{ width: '100%', height: '300px' }} tabIndex={0} aria-label="BloomWatch Map" />
  );
};

export default Map2D;