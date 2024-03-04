import React, { useEffect, useState } from 'react';
import axios from 'axios';
import DistributionStatistics from "../DistrubutionStatistic";

interface Distribution {
  id: number;
  name: string;
  message: string;
}

const DistributionList: React.FC = () => {
  const [distributions, setDistributions] = useState<Distribution[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios('http://localhost:8000/api/distribution/');
        setDistributions(result.data);
      } catch (error) {
        console.error('Ошибка при получении данных о рассылках:', error);
      }
    };
    fetchData();
    const intervalId = setInterval(fetchData, 10000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h2>Distributions</h2>
      {distributions.map(distribution => (
        <div key={distribution.id}>
          <h3>{distribution.name}</h3>
          <p>{distribution.message}</p>
          {/* Вставляем компонент статистики, передавая id рассылки */}
          <DistributionStatistics distributionId={distribution.id} />
        </div>
      ))}
    </div>
  );
};

export default DistributionList;

