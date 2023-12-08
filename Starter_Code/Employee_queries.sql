--List the employee number, last name, first name, sex, and salary of each employee.
select
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from
	employees as e
	join salaries as s on e.emp_no = s.emp_no
order by
	s.salary desc;

--List the first name, last name, and hire date for the employees who were hired in 1986
select
	e.first_name,
	e.last_name,
	e.hire_date
from
	employees as e
where extract(year from e.hire_date) = 1986;

--List the manager of each department along with their department number, department name, employee number, last name, and first name
select
	d.dept_no,
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
from
	employees as e
	join dept_manager as dm on e.emp_no = dm.emp_no
	join departments as d on dm.dept_no = d.dept_no
order by
	dm.dept_manager_id;

--List the department number for each employee along with that employee’s employee number, last name, first name, and department name
select
	d.dept_no,
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on de.dept_no = d.dept_no

order by
	d.dept_name;

--List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B
select
	e.first_name,
	e.last_name,
	e.sex
from
	employees as e
where
	first_name = 'Hercules'
	and last_name like 'B%'
order by 
	last_name;

--List each employee in the Sales department, including their employee number, last name, and first name
select
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on de.dept_no = d.dept_no
where
	d.dept_name in ('Sales')
order by 
	e.emp_no asc;

--List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name
select
	d.dept_name,
	e.emp_no,
	e.last_name,
	e.first_name
from
	employees as e
	join dept_emp as de on e.emp_no = de.emp_no
	join departments as d on de.dept_no = d.dept_no
where
	d.dept_name in ('Sales', 'Development')
order by 
	d.dept_name asc, e.emp_no asc;

--List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name)
select
	e.last_name,
	count(e.emp_no) as name_count
from
	employees as e
group by 
	e.last_name
order by 
	count(e.emp_no) desc;