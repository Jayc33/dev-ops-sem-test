@extends('layouts.app')

@section('content')
    <div class="d-flex justify-content-center mt-2 mb-4">
        <img style="width: 70px" src="https://vuejs.org/images/logo.svg?_sw-precache=346e12ee28bb0e5f5600d47beb4c7a47">
    </div>
    <div id='app'>
        <example-component></example-component>    
    </div>    
    <script src="{{ mix('/js/app.js') }}"></script>
@endsection