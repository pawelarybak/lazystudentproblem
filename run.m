clc
clear
close all

% data2;
[ subjects, semesters, max_times, min_points] = genRandomData(100, [1 10], [1 15], [5 10]);

filename = 'data.txt';

str = generate_string(subjects, semesters, max_times, min_points);

fileID = fopen(filename,'w');
fprintf(fileID, str);
fclose(fileID);

[status, result] = system(['run_file.py ' filename]);

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

if(~exist('./fig/', 'dir'))
	mkdir('./fig/');
end

figure
	hold on
	bar(time,'stacked');
	plot(-1:semesters+1, ones(1, semesters+3)*max_times(1))
	title('Czas poœwiêcony na naukê')
	xlabel('Semestr')
	axis([0.6 semesters+0.4 -Inf Inf])
	print('./fig/1.png', '-dpng')

figure
	hold on
	plot(1:semesters, points, '-o');
	plot(-1:semesters+1, ones(1, semesters+3)*min_points)
	title('Zdobyte punkty')
	xlabel('Semestr')
	axis([0.6 semesters+0.4 0 Inf])
	print('./fig/2.png', '-dpng')

min_vals = dlmread('min.csv', ' ');

out_of_limits = dlmread('out_of_limits.csv', ' ');

figure
	plot(min_vals(:, 1), min_vals(:, 2))
	title('Minimalna wartoœæ funkcji celu')
	xlabel('Numer generacji')
	print('./fig/3.png', '-dpng')
	
figure
	plot(out_of_limits(:, 1), out_of_limits(:, 2))
	title('Iloœæ osobników nie spe³niaj¹ca ograniczeñ')
	xlabel('Numer generacji')
	print('./fig/4.png', '-dpng')