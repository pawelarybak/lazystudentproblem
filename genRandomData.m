function [ subjects, semesters, max_times, min_points] = genRandomData(no_subjects, time_lim, point_lim, semester_lim)
	subjects = rand(no_subjects, 2);
	subjects(:, 1) = round(subjects(:, 1) * (time_lim(2) - time_lim(1))) + time_lim(1);
	subjects(:, 2) = round(subjects(:, 2) * (point_lim(2) - point_lim(1))) + point_lim(1);
	semesters = round(rand*(semester_lim(2) - semester_lim(1))) + semester_lim(1);
	averages = zeros(no_subjects, 1);
	for i = 1:no_subjects
		averages(i) = subjects(i, 1)/subjects(i, 2);
	end
	ratio_avg = mean(averages);
	time_sum =  sum(subjects(:, 1));
	min_points = time_sum/4 + round((time_sum/2)*rand);
	time_const = round((min_points/semesters)*ratio_avg);
	time_const = time_const - rand*(time_const/4);
	max_times = ones(1, semesters)*time_const;
end

