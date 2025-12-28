from flask import Blueprint, render_template, jsonify, request
import datetime

main = Blueprint('main', __name__)

# In-memory task storage (we'll add database later)
tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "description": "Master containerization",
        "completed": False,
        "created_at": "2024-12-27"
    },
    {
        "id": 2,
        "title": "Setup CI/CD Pipeline",
        "description": "Automate deployments with GitHub Actions",
        "completed": True,
        "created_at": "2024-12-26"
    },
    {
        "id": 3,
        "title": "Deploy to Production",
        "description": "Push to Docker Hub and deploy",
        "completed": False,
        "created_at": "2024-12-27"
    }
]

@main.route('/')
def index():
    """Home page with task manager UI"""
    return render_template('index.html', tasks=tasks)

@main.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0",
        "service": "flask-task-manager"
    })

@main.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify({
        "success": True,
        "data": tasks,
        "count": len(tasks)
    })

@main.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get single task by ID"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify({"success": True, "data": task})
    return jsonify({"success": False, "error": "Task not found"}), 404

@main.route('/api/tasks', methods=['POST'])
def add_task():
    """Create new task"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({
            "success": False,
            "error": "Title is required"
        }), 400
    
    new_task = {
        "id": max([t['id'] for t in tasks]) + 1 if tasks else 1,
        "title": data.get('title'),
        "description": data.get('description', ''),
        "completed": False,
        "created_at": datetime.datetime.now().strftime('%Y-%m-%d')
    }
    
    tasks.append(new_task)
    
    return jsonify({
        "success": True,
        "data": new_task,
        "message": "Task created successfully"
    }), 201

@main.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update existing task"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({
            "success": False,
            "error": "Task not found"
        }), 404
    
    data = request.get_json()
    
    if 'title' in data:
        task['title'] = data['title']
    if 'description' in data:
        task['description'] = data['description']
    if 'completed' in data:
        task['completed'] = data['completed']
    
    return jsonify({
        "success": True,
        "data": task,
        "message": "Task updated successfully"
    })

@main.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete task"""
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({
            "success": False,
            "error": "Task not found"
        }), 404
    
    tasks = [t for t in tasks if t['id'] != task_id]
    
    return jsonify({
        "success": True,
        "message": "Task deleted successfully"
    })

@main.route('/api/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({
            "success": False,
            "error": "Task not found"
        }), 404
    
    task['completed'] = not task['completed']
    
    return jsonify({
        "success": True,
        "data": task,
        "message": f"Task marked as {'completed' if task['completed'] else 'incomplete'}"
    })