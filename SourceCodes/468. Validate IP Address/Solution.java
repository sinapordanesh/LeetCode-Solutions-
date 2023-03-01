package com.sina.leetCode;

import java.lang.reflect.Array;
import java.util.*;

class Solution {
    public String validIPAddress(String queryIP) {

        if (queryIP.contains(".")){
            if (ipv4Identifier(queryIP)){
                return "IPv4";
            }
        } else if (queryIP.contains(":")){
            if (ipv6Identifier(queryIP)){
                return "IPv6";
            }
        }

        return "Neither";
    }

    public boolean ipv4Identifier(String ip){

        if (ip.charAt(ip.length()-1) == '.' || ip.charAt(0) == '.'){
            return false;
        }

        String[] parts = ip.split("\\.");


        if (parts.length != 4){
            return false;
        }

        for (String part: parts) {

            try{
                Integer.parseInt(part);
            } catch (Exception e){
                return false;
            }

            if (Integer.parseInt(part) > 255) {
                return false;
            } else {
                if (Integer.parseInt(part) > 99) {
                    if (part.length() != 3) {
                        return false;
                    }
                } else if (Integer.parseInt(part) <= 99 && Integer.parseInt(part) > 9) {
                    if (part.length() != 2) {
                        return false;
                    }
                } else if (Integer.parseInt(part) >= 0 && Integer.parseInt(part) <= 9) {
                    if (part.length() != 1) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public boolean ipv6Identifier(String ip){

        String validation = "0123456789abcdefABCDEF";

        String[] parts = ip.split(":");

        if (ip.charAt(ip.length()-1) == ':' || ip.charAt(0) == ':'){
            return false;
        }

        if (parts.length != 8){
            return false;
        }

        for(String part: parts){
            if (part.length() == 0 || part.length() > 4){
                return false;
            }
            for (int i = 0; i < part.length(); i++) {

                if (!validation.contains(String.valueOf(part.charAt(i)))){
                    return false;
                }
            }
        }
        return true;
    }
}