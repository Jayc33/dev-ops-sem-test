<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Exception;

class TestController extends Controller
{
    public function throwsError(Request $request)
    {
        throw new Exception("Dang it!");
    }

    public function takesAWhile(Request $request)
    {
        sleep(rand(2, 4));
        return redirect("/");
    }

    public function noProblemsHere(Request $request)
    {
        return redirect("/");
    }
}
