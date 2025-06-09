import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch('https://glowing-trout-4jq99rvj6vxw2q5j5-8000.app.github.dev/api/leaderboard/')
      .then(res => res.json())
      .then(data => setEntries(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 display-6">Leaderboard</h2>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>User</th>
                <th>Points</th>
                <th>Rank</th>
              </tr>
            </thead>
            <tbody>
              {entries.map((entry, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{entry.user}</td>
                  <td>{entry.points}</td>
                  <td>{entry.rank}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
