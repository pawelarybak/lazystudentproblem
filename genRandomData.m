function [ subjects, semesters, max_times, min_points] = genRandomData(no_subjects, time_lim, point_lim, semester_lim)
	subjects = rand(no_subjects, 2);
	subjects(:, 1) = round(subjects(:, 1) * (time_lim(2) - time_lim(1))) + time_lim(1);
	subjects(:, 2) = round(subjects(:, 2) * (point_lim(2) - point_lim(1))) + point_lim(1);
	semesters = round(rand*(semester_lim(2) - semester_lim(1))) + semester_lim(1);
	max_times = ones(1, semesters)*50;
	min_points = 400;
end

