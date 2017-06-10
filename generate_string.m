function [ str ] = generate_string( subjects, semesters, max_times, min_points)
	str = 'subjects = [';
	for i = 1:size(subjects, 1)
		str = [str 'Subject(' num2str(i) ', ' num2str(subjects(i, 1)) ', ' num2str(subjects(i, 2)) '),\n'];
	end
	str = [str ']\n'];
	str = [str 'semesters = ' num2str(semesters) '\n'];
	str = [str 'max_times = ['];
	for i = 1:length(max_times)
		str = [str num2str(max_times(i)) ', '];
	end
	str = [str ']\n'];
	str =[str 'min_points = ' num2str(min_points) ' \n'];
end

