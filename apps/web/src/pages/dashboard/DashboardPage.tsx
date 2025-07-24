import React from 'react';
import {
  Box,
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Chip,
  LinearProgress,
} from '@mui/material';
import { PlayArrow, CloudUpload, Timeline, Group } from '@mui/icons-material';

// Mock data for development
const mockStats = {
  totalSessions: 12,
  processingQueue: 3,
  completedAnalyses: 9,
  activeTeams: 2,
};

const mockRecentSessions = [
  {
    id: '1',
    name: 'Training Session - Week 3',
    team: 'Ravens FC',
    status: 'completed',
    progress: 100,
    duration: '90 min',
    createdAt: '2024-01-20',
  },
  {
    id: '2',
    name: 'Match vs Eagles',
    team: 'Ravens FC',
    status: 'processing',
    progress: 65,
    duration: '95 min',
    createdAt: '2024-01-19',
  },
  {
    id: '3',
    name: 'Tactical Practice',
    team: 'Hawks United',
    status: 'uploading',
    progress: 25,
    duration: '60 min',
    createdAt: '2024-01-18',
  },
];

const getStatusColor = (status: string): 'success' | 'warning' | 'info' => {
  switch (status) {
    case 'completed':
      return 'success';
    case 'processing':
      return 'warning';
    case 'uploading':
      return 'info';
    default:
      return 'info';
  }
};

export const DashboardPage: React.FC = () => {
  return (
    <Box>
      <Typography variant="h4" component="h1" gutterBottom>
        Dashboard
      </Typography>
      <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
        Welcome to Trackball - Your AI-powered sports analysis platform
      </Typography>

      {/* Stats Cards */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <PlayArrow sx={{ fontSize: 40, color: 'primary.main', mb: 1 }} />
              <Typography variant="h4" component="div">
                {mockStats.totalSessions}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Total Sessions
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <CloudUpload sx={{ fontSize: 40, color: 'warning.main', mb: 1 }} />
              <Typography variant="h4" component="div">
                {mockStats.processingQueue}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Processing Queue
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Timeline sx={{ fontSize: 40, color: 'success.main', mb: 1 }} />
              <Typography variant="h4" component="div">
                {mockStats.completedAnalyses}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Completed Analyses
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Group sx={{ fontSize: 40, color: 'info.main', mb: 1 }} />
              <Typography variant="h4" component="div">
                {mockStats.activeTeams}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Active Teams
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Recent Sessions */}
      <Typography variant="h5" component="h2" gutterBottom>
        Recent Sessions
      </Typography>

      <Grid container spacing={3}>
        {mockRecentSessions.map((session) => (
          <Grid item xs={12} md={6} lg={4} key={session.id}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
                  <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    {session.name}
                  </Typography>
                  <Chip
                    label={session.status}
                    color={getStatusColor(session.status)}
                    size="small"
                  />
                </Box>

                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Team: {session.team}
                </Typography>

                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Duration: {session.duration}
                </Typography>

                <Typography variant="body2" color="text.secondary" gutterBottom>
                  Created: {session.createdAt}
                </Typography>

                {session.status !== 'completed' && (
                  <Box sx={{ mt: 2 }}>
                    <Typography variant="body2" color="text.secondary" gutterBottom>
                      Progress: {session.progress}%
                    </Typography>
                    <LinearProgress
                      variant="determinate"
                      value={session.progress}
                      sx={{ height: 8, borderRadius: 4 }}
                    />
                  </Box>
                )}
              </CardContent>

              <CardActions>
                <Button
                  size="small"
                  startIcon={<PlayArrow />}
                  disabled={session.status !== 'completed'}
                >
                  View Analysis
                </Button>
                <Button size="small" color="primary">
                  Details
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* Quick Actions */}
      <Box sx={{ mt: 4, textAlign: 'center' }}>
        <Typography variant="h6" gutterBottom>
          Quick Actions
        </Typography>
        <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center', flexWrap: 'wrap' }}>
          <Button
            variant="contained"
            startIcon={<CloudUpload />}
            size="large"
          >
            Upload Video
          </Button>
          <Button
            variant="outlined"
            startIcon={<Group />}
            size="large"
          >
            Manage Teams
          </Button>
          <Button
            variant="outlined"
            startIcon={<Timeline />}
            size="large"
          >
            View Analytics
          </Button>
        </Box>
      </Box>
    </Box>
  );
};