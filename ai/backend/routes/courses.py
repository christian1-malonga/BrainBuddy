from flask import Blueprint, jsonify, request
from models.course import Course, Lesson, Assignment, db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses', methods=['GET'])
def get_all_courses():
    """Get all courses"""
    try:
        courses = Course.query.all()
        courses_data = []
        
        for course in courses:
            course_dict = course.to_dict()
            
            # Get lessons for this course
            lessons = Lesson.query.filter_by(course_id=course.id).order_by(Lesson.order_index).all()
            course_dict['lessons'] = [lesson.to_dict() for lesson in lessons]
            
            # Get assignments for this course
            assignments = Assignment.query.filter_by(course_id=course.id).all()
            course_dict['assignments'] = [assignment.to_dict() for assignment in assignments]
            
            # Calculate progress (mock data for now)
            total_lessons = len(lessons)
            completed_lessons = len([l for l in lessons if l.order_index < total_lessons * 0.7])  # Mock completion
            course_dict['completedLessons'] = completed_lessons
            course_dict['progress'] = int((completed_lessons / total_lessons * 100)) if total_lessons > 0 else 0
            course_dict['nextDeadline'] = '2024-01-15'  # Mock deadline
            
            courses_data.append(course_dict)
        
        return jsonify(courses_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get specific course details"""
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404
        
        course_dict = course.to_dict()
        
        # Get lessons for this course
        lessons = Lesson.query.filter_by(course_id=course.id).order_by(Lesson.order_index).all()
        course_dict['lessons'] = [lesson.to_dict() for lesson in lessons]
        
        # Get assignments for this course
        assignments = Assignment.query.filter_by(course_id=course.id).all()
        course_dict['assignments'] = [assignment.to_dict() for assignment in assignments]
        
        return jsonify(course_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@courses_bp.route('/courses', methods=['POST'])
def create_course():
    """Create new course"""
    try:
        data = request.get_json()
        course = Course(
            title=data.get('title'),
            instructor=data.get('instructor'),
            description=data.get('description'),
            category=data.get('category'),
            difficulty=data.get('difficulty'),
            estimated_hours=data.get('estimated_hours'),
            total_lessons=data.get('total_lessons', 0)
        )
        db.session.add(course)
        db.session.commit()
        return jsonify(course.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@courses_bp.route('/courses/<int:course_id>/lessons', methods=['POST'])
def create_lesson():
    """Create new lesson for a course"""
    try:
        data = request.get_json()
        lesson = Lesson(
            course_id=data.get('course_id'),
            title=data.get('title'),
            duration=data.get('duration'),
            lesson_type=data.get('type', 'video'),
            order_index=data.get('order_index', 0)
        )
        db.session.add(lesson)
        db.session.commit()
        return jsonify(lesson.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@courses_bp.route('/courses/<int:course_id>/assignments', methods=['POST'])
def create_assignment():
    """Create new assignment for a course"""
    try:
        data = request.get_json()
        assignment = Assignment(
            course_id=data.get('course_id'),
            title=data.get('title'),
            due_date=data.get('due_date'),
            status=data.get('status', 'upcoming'),
            grade=data.get('grade')
        )
        db.session.add(assignment)
        db.session.commit()
        return jsonify(assignment.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

