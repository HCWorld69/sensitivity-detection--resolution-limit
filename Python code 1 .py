%%%% My MATLAB code for generating a typical SEM EDX spectra of a random element of my choice (in this example, I will choose carbon) using the given parameters:

%%% This code generates a SEM EDX spectrum for carbon using the given parameters, and then plots the spectrum. It also calculates and prints the sensitivity, detection limit, maximum achievable resolution, and minimum limit for the spectrum. Note that the values used in this code are just examples, and you may need to adjust them for your specific experiment.


% Define the parameters
E0 = 15; % Accelerating voltage in keV
takeoff_angle = 35; % Take-off angle in degrees
detection_angle = 35; % Detection angle in degrees
beam_current = 10; % Beam current in nA
dwell_time = 10; % Dwell time in ms
spectral_range = 0:2047; % Spectral range in channels
peak_position = 270; % Peak position in channels
peak_amplitude = 100; % Peak amplitude in counts
FWHM = 30; % Full width at half maximum in channels
background = 20; % Background count level

% Generate the spectrum
spectrum = zeros(size(spectral_range));
for i = 1:length(spectral_range)
    channel_energy = E0 * (spectral_range(i) + 0.5) / 2048;
    solid_angle = sin(takeoff_angle * pi / 180) / sin(detection_angle * pi / 180);
    incident_flux = beam_current / (1.6e-19 * dwell_time);
    sensitivity = 0.1; % Sensitivity in counts/nA
    spectral_response = exp(-(spectral_range(i) - peak_position)^2 / (2 * FWHM^2));
    spectrum(i) = background + sensitivity * solid_angle * incident_flux * spectral_response;
end

% Plot the spectrum
figure;
plot(spectral_range, spectrum);
xlabel('Channel');
ylabel('Counts');
title('SEM EDX Spectrum for Carbon');

% Calculate the sensitivity, detection limit, maximum achievable resolution, and minimum limit
sensitivity = peak_amplitude / (beam_current * dwell_time);
detection_limit = 3 * background / sensitivity;
maximum_resolution = E0 / (2 * FWHM);
minimum_limit = (E0 * 0.1) / (2 * FWHM); % Assumes a 10% energy resolution
fprintf('Sensitivity: %.2f counts/nA\n', sensitivity);
fprintf('Detection Limit: %.2f ng/cm^2\n', detection_limit);
fprintf('Maximum Achievable Resolution: %.2f eV\n', maximum_resolution);
fprintf('Minimum Limit: %.2f %%\n', minimum_limit);
