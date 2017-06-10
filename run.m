clc
clear
close all

% data2;

subject_size = 100;
time_limits = [1 10];
point_limits = [1 15];
semester_limits = [5 10];

[ subjects, semesters, max_times, min_points] = genRandomData(subject_size, time_limits, point_limits, semester_limits);

filename = 'data.txt';

str = generate_string(subjects, semesters, max_times, min_points);

fileID = fopen(filename,'w');
fprintf(fileID, str);
fclose(fileID);

if ispc()
	[status, result] = system(['run_file.py ' filename]);
else
	[status, result] = system(['./run_file.py ' filename]);
end

k = strfind(result,'hof = ');

eval(result(k:end));

semester_container = cell(semesters, 1);

for i = 1:semesters
	semester_container{i} = [];
end

for i = 1:length(hof)
	if hof(i)
		semester_container{hof(i)} = [semester_container{hof(i)} , i];
	end
end

len = 0;
for i = 1:semesters
	if length(semester_container{i})>len
		len = length(semester_container{i});
	end
end

points = zeros(semesters, 1);
time = zeros(semesters, len);
for i = 1:semesters
	for j = 1:length(semester_container{i})
		points(i) = points(i) + subjects(semester_container{i}(j), 2);
		time(i, j) = subjects(semester_container{i}(j), 1);
	end
	if i ~= semesters
		points(i+1) = points(i);
	end
end

dir = ['./fig/' num2str(subject_size) '/'];
if(~exist(dir, 'dir'))
	mkdir(dir);
end

DateString = datestr(datetime, 'dd_HH_MM_SS_');
path = [dir DateString];

figure
	hold on
	bar(time,'stacked');
	plot(-1:semesters+1, ones(1, semesters+3)*max_times(1))
	title('Czas po�wi�cony na nauk�')
	xlabel('Semestr')
	axis([0.6 semesters+0.4 -Inf Inf])
	print([path '1.png'], '-dpng')

figure
	hold on
	plot(1:semesters, points, '-o');
	plot(-1:semesters+1, ones(1, semesters+3)*min_points)
	title('Zdobyte punkty')
	xlabel('Semestr')
	axis([0.6 semesters+0.4 0 Inf])
	print([path '2.png'], '-dpng')

min_vals = dlmread('min.csv', ' ');

out_of_limits = dlmread('out_of_limits.csv', ' ');

figure
	plot(min_vals(:, 1), min_vals(:, 2))
	title('Minimalna warto�� funkcji celu')
	xlabel('Numer generacji')
	print([path '3.png'], '-dpng')
	
figure
	plot(out_of_limits(:, 1), out_of_limits(:, 2))
	title('Ilo�� osobnik�w nie spe�niaj�ca ogranicze�')
	xlabel('Numer generacji')
	print([path '4.png'], '-dpng')