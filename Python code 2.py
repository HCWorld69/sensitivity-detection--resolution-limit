clc
clear all
format compact
%%%%%%%%%%%  CODE: My matlab code for a typical input and output signa using the following. Assume values as per your need. Also plot : 
 % sensitivity detection limit maximum achievable resolution minimum limit

% Generate a signal
Fs = 1000; % Sampling rate (Hz)
t = 0:1/Fs:1-1/Fs; % Time vector (s)
f = 10; % Signal frequency (Hz)
A = 1; % Signal amplitude
x = A*sin(2*pi*f*t); % Signal

% Set parameters
SNR = 20; % Signal-to-noise ratio (dB)
detectionThreshold = 0.5; % Detection threshold (normalized amplitude)
resolution = 0.01; % Resolution (normalized amplitude)

% Add noise to signal
sigma = A/(10^(SNR/20)); % Standard deviation of noise
n = sigma*randn(size(x)); % Gaussian noise
y = x + n; % Noisy signal

% Plot signal and noise
figure;
subplot(2,1,1);
plot(t, x, 'b', t, y, 'r');
xlabel('Time (s)');
ylabel('Amplitude');
legend('Signal', 'Noisy signal');

% Compute sensitivity, detection limit, maximum achievable resolution, and minimum limit
sensitivity = A/sigma;
detectionLimit = detectionThreshold*sigma;
maximumAchievableResolution = sigma*resolution;
minimumLimit = sigma/sensitivity;

% Plot parameters
subplot(2,1,2);
bar([sensitivity, detectionLimit, maximumAchievableResolution, minimumLimit]);
set(gca, 'XTick', 1:4, 'XTickLabel', {'Sensitivity', 'Detection limit', 'Max resolution', 'Min limit'});
ylabel('Value');
