import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Определение типа для статистики рассылки
interface DistributionStatisticsProps {
  distributionId: number;
}

interface Statistics {
  total_users: number;
  messages_sent: number;
}

const DistributionStatistics: React.FC<DistributionStatisticsProps> = ({ distributionId }) => {
  const [statistics, setStatistics] = useState<Statistics | null>(null);

  useEffect(() => {
    const fetchStatistics = async () => {
      try {
        const result = await axios(`http://localhost:8000/api/distribution/${distributionId}/statistics/`);
        setStatistics(result.data);
      } catch (error) {
        console.error('Ошибка при получении статистики рассылки:', error);
      }
    };
    fetchStatistics();
        // Запускаем опрос статистики каждые 10 секунд
    const intervalId = setInterval(fetchStatistics, 10000);

    // Очистка интервала при размонтировании компонента
    return () => clearInterval(intervalId);
  }, [distributionId]);

  if (!statistics) {
    return <div>Loading statistics...</div>;
  }

  return (
    <div>
      <h3>Статистика рассылки</h3>
      <p>Общее количество пользователей: {statistics.total_users}</p>
      <p>Сообщений отправлено: {statistics.messages_sent}</p>
    </div>
  );
};

export default DistributionStatistics;
