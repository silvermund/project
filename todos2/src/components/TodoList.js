import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { deleteTodoAction, toggleTodoAction } from '../store/todo.reducer'


const TodoList = () => {
    const todos = useSelector( state => state.todos )
    const dispatch = useDispatch()
    const toggleTodo = id => dispatch(toggleTodoAction(id))
    const deleteTodo = id =>
}