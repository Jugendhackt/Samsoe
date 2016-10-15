<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import="javax.servlet.http.HttpServletResponse" %>
<%@ page import="java.util.List" %>
<%@ page import="ajaxdemo.co" %>
<%
String data = request.getParameter("qrdata");
String antwort = co.main(data);
%>
<%= antwort %>
