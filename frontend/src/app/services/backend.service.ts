import {Injectable} from '@angular/core'
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import {map} from 'rxjs/operators';
import {environment} from '../../environments/environment';

@Injectable()
export class BackendService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // Very important to define a responsetype
  deviceRec(): Observable<any> {
    return this.http
      .get(`${environment.apiUrl}/device`,{responseType: 'text'})
  }

  // Very important to define a responsetype
  aboutUs(): Observable<any> {
    return this.http
      .get(`${environment.apiUrl}/about`,{responseType: 'text'});
  }
}