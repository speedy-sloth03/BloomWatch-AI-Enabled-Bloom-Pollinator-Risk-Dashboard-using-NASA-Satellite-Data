import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

const divisions = [
  { id: 'Dhaka', name_en: 'Dhaka', name_bn: 'ঢাকা', bbox: [22.0, 88.0, 24.5, 91.0] },
  { id: 'Chattogram', name_en: 'Chattogram', name_bn: 'চট্টগ্রাম', bbox: [20.5, 91.5, 23.5, 92.8] },
  { id: 'Khulna', name_en: 'Khulna', name_bn: 'খুলনা', bbox: [21.2, 88.0, 23.0, 90.5] },
  { id: 'Rajshahi', name_en: 'Rajshahi', name_bn: 'রাজশাহী', bbox: [24.0, 88.0, 26.5, 89.8] },
  { id: 'Barishal', name_en: 'Barishal', name_bn: 'বরিশাল', bbox: [21.0, 89.5, 22.5, 90.9] },
  { id: 'Sylhet', name_en: 'Sylhet', name_bn: 'সিলেট', bbox: [24.3, 91.5, 26.0, 92.9] },
  { id: 'Rangpur', name_en: 'Rangpur', name_bn: 'রংপুর', bbox: [24.0, 88.0, 26.0, 89.7] },
  { id: 'Mymensingh', name_en: 'Mymensingh', name_bn: 'ময়মনসিংহ', bbox: [24.0, 89.5, 25.5, 90.8] }
];

const CesiumGlobe = () => {
  const globeRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!window.Cesium) return;
    // Minimal Cesium globe setup
    const Cesium = window.Cesium;
    if (!Cesium) return;
    const viewer = new Cesium.Viewer(globeRef.current!, {
      imageryProvider: new Cesium.IonImageryProvider({ assetId: 2 }),
      homeButton: false,
      timeline: false,
      animation: false,
      sceneModePicker: false
    });
    // Center over Bangladesh
    viewer.camera.setView({
      destination: Cesium.Cartesian3.fromDegrees(90.4, 23.7, 2e6)
    });
    // Add region overlays + click handlers
    divisions.forEach((div, i) => {
      // Create simple rectangle for each bbox
      const entity = viewer.entities.add({
        rectangle: {
          coordinates: Cesium.Rectangle.fromDegrees(...div.bbox),
          material: Cesium.Color.fromCssColorString('#005f73').withAlpha(0.3)
        },
        name: div.name_en,
        id: div.id
      });
      entity.description = `${div.name_en} (${div.name_bn})`;
      entity.label = {
        text: `${div.name_en}\n${div.name_bn}`,
        font: '16px sans-serif',
        fillColor: Cesium.Color.WHITE,
        showBackground: true
      };
    });
    // Pick handler
    viewer.screenSpaceEventHandler.setInputAction((movement: any) => {
      const picked = viewer.scene.pick(movement.position);
      if (Cesium.defined(picked) && picked.id && picked.id.id) {
        navigate(`/dashboard?region=${picked.id.id}`);
      }
    }, Cesium.ScreenSpaceEventType.LEFT_CLICK);

    return () => {
      viewer.destroy();
    };
  }, [navigate]);

  // Keyboard ARIA: allow region selection
  useEffect(() => {
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === 'Enter') {
        const region = divisions[0].id;
        navigate(`/dashboard?region=${region}`);
      }
    };
    window.addEventListener('keydown', handleKey);
    return () => window.removeEventListener('keydown', handleKey);
  }, [navigate]);

  return (
    <div ref={globeRef} style={{ width: '100%', height: '500px', outline: 'none' }}
      tabIndex={0} aria-label="Bangladesh Globe, select division" />
  );
};

export default CesiumGlobe;